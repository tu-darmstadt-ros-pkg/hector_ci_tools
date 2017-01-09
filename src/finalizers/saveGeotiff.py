from abstractFinalizer import AbstractFinalizer
import rospy
from std_msgs.msg import String

from ci_tools.helpers.ci_log import CiLog


class SaveGeotiff(AbstractFinalizer):
    def __init__(self):
        print "init"

    @staticmethod
    def final_action():
        CiLog.info("[finalizers.SaveGeotiff]: Saving GeoTiff...")
        sys_command_publisher = rospy.Publisher("syscommand", String, queue_size=5)
        geotiff_string = "savegeotiff"
        sys_command_publisher.publish(geotiff_string)
