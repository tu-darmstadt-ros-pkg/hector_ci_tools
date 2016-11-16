#!/usr/bin/env python
from ci_tools.ciTools import SimulationControl


class HectorSimulationControl(SimulationControl):
    """Class for controlling the simulation with Hector Tracker setup."""

    def __init__(self):
        """Initialize variables, then start sim with behavior."""
        super(HectorSimulationControl, self).__init__()
        self.import_finalizers()
        self.start_sim_with_behavior()

    def import_finalizers(self,):
        """Import of finalizer classes that will be executed."""
        if len(self._mission_finalizers) > 0:
            mission_finalizers_list = self._mission_finalizers.split(",")
            for mission_finalizer in mission_finalizers_list:
                module_class = mission_finalizer.split(".")
                module = __import__('finalizers.' + module_class[0], fromlist=[module_class[1]])
                self._finalizer_classes.append(getattr(module, module_class[1]))
