import fedml
from fedml.simulation import SimulatorMPI
from data.data_loader import load_data
from model.autoencoder import AutoEncoder
from trainer.fed_detect_trainer import MyModelTrainer


if __name__ == "__main__":
    # init FedML framework
    args = fedml.init()

    # init device
    device = fedml.device.get_device(args)

    # load data
    dataset, output_dim = load_data(args)

    # load model
    model = AutoEncoder(output_dim)

    # create trainer
    trainer = MyModelTrainer(model)

    # start training
    simulator = SimulatorMPI(args, device, dataset, model, trainer)
    simulator.run()