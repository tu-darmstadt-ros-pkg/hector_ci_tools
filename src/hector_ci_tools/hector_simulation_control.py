#!/usr/bin/env python
import rospy
from ci_tools.simulation_control import SimulationControl
from ci_tools.helpers.ci_log import CiLog


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
        CiLog.info("Initialization finished. Starting timer")
        self.start_simulation_timer()



    def read_ros_additional_ros_params(self):
        """Reads additional ROS parameters that are not considered by SimulationControl.read_ros_additional_ros_params()."""
        mission_behavior_full_param_name = rospy.search_param('mission_behavior')
        self._mission_behavior = str(rospy.get_param(mission_behavior_full_param_name))
