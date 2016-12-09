#!/usr/bin/env python
from ci_tools.ciTools import SimulationControl
import rospy
from helpers.hector_ci_loginfo import HectorCiLogInfo


class HectorSimulationControl(SimulationControl):
    """Class for controlling the simulation with Hector Tracker setup."""

    def __init__(self):
        """Initialize variables, then start sim with behavior."""
        super(HectorSimulationControl, self).__init__()
        self._mission_behavior = ""

        self.read_ros_additional_ros_params()
        self.import_finalizers()

        self.start_sim()
        self.start_behavior(self._mission_behavior)
        HectorCiLogInfo.log("Initialization finished.")

    def import_finalizers(self,):
        """Import of finalizer classes that will be executed."""
        if len(self._mission_finalizers) > 0:
            mission_finalizers_list = self._mission_finalizers.split(",")
            for mission_finalizer in mission_finalizers_list:
                module_class = mission_finalizer.split(".")
                module = __import__('finalizers.' + module_class[0], fromlist=[module_class[1]])
                self._finalizer_classes.append(getattr(module, module_class[1]))

    def read_ros_additional_ros_params(self):
        """Reads additional ROS parameters that are not considered by SimulationControl.read_ros_additional_ros_params()."""
        mission_behavior_full_param_name = rospy.search_param('mission_behavior')
        self._mission_behavior = str(rospy.get_param(mission_behavior_full_param_name))
