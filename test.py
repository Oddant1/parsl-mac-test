import parsl

from parsl.config import Config
from parsl.channels import LocalChannel
from parsl.providers import SlurmProvider, AdHocProvider
from parsl.executors import HighThroughputExecutor
from parsl.launchers import SrunLauncher

config = Config(
    strategy='None',
    executors=[
        HighThroughputExecutor(
            label='default',
            max_workers=10,
            provider=SlurmProvider(
                launcher=SrunLauncher(),
                channel=LocalChannel()),
        ),
        HighThroughputExecutor(
            label='other',
            max_workers=10,
            provider=AdHocProvider(
                channel=LocalChannel()
            )
        )
    ])

parsl.load(config)
