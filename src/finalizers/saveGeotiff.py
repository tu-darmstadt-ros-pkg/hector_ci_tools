from abstractFinalizer import AbstractFinalizer
import rospy
from std_msgs.msg import String


class SaveGeotiff(AbstractFinalizer):
    def __init__(self):
        print "init"

    @staticmethod
    def final_action():
        rospy.loginfo("[argo_ci_tools][finalizers.SaveGeotiff]: Saving GeoTiff...")
        sys_command_publisher = rospy.Publisher("syscommand", String, queue_size=5)
        geotiff_string = String()
        geotiff_string = "savegeotiff"
        sys_command_publisher.publish(geotiff_string)
