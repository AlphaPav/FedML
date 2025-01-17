import logging
import fedml
import torch
from fedml.cross_silo import Client
from trainer.detection_trainer import DetectionTrainer
from utils.init_yolo import init_yolo


if __name__ == "__main__":
    # init FedML framework
    args = fedml.init()

    # init device
    device = fedml.device.get_device(args)
    logging.info("Device: {}".format(device))

    # init yolo
    model, dataset, args = init_yolo(args=args, device=device)
    logging.info("init model, dataset and args done")

    # trainer
    trainer = DetectionTrainer(model=model, args=args)
    logging.info("init trainer done")

    # start training
    client = Client(args, device, dataset, model, model_trainer=trainer)
    logging.info("init client done")
    client.run()
