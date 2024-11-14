import parsl

from parsl.config import Config
from parsl.providers import SlurmProvider
from parsl.executors import HighThroughputExecutor
from parsl.launchers import SrunLauncher
from parsl.addresses import address_by_interface

config = Config(
    executors=[
        HighThroughputExecutor(
            label="frontera_htex",
            address=address_by_interface('ib0'),
            max_workers_per_node=56,
            provider=SlurmProvider(
                nodes_per_block=128,
                init_blocks=1,
                partition='normal',
                launcher=SrunLauncher(),
            ),
        )
    ],
)

parsl.load(config)
