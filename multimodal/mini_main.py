from __future__ import print_function
import argparse
import yaml

from logger import Logger
from trainers.selfsupervised_depth import selfsupervised_depth
from trainers.selfsupervised_origin import selfsupervised_origin

if __name__ == "__main__":

    # Load the config file
    parser = argparse.ArgumentParser(description="Sensor fusion model")
    parser.add_argument("--config", help="YAML config file")
    parser.add_argument("--notes", default="", help="run notes")
    parser.add_argument("--dev", type=bool, default=False, help="run in dev mode")
    parser.add_argument(
        "--continuation",
        type=bool,
        default=False,
        help="continue a previous run. Will continue the log file",
    )
    args = parser.parse_args()

    # Add the yaml to the config args parse
    with open(args.config) as f:
        configs = yaml.load(f)

    # Merge configs and args
    for arg in vars(args):
        configs[arg] = getattr(args, arg)
    useDepth = configs['usingDepth']
    # Initialize the loggers
    logger = Logger(configs)

    # Initialize the trainer
    print("USING DEPTH", useDepth)
    if useDepth:
        trainer = selfsupervised_depth(configs, logger)
    else:
        trainer = selfsupervised_origin(configs, logger)
    trainer.train()
