import rospy


class HectorCiLogInfo(object):
    """Helper methods regarding logging."""

    @staticmethod
    def log(message):
        """Uses rospy.loginfo() to post message with additional"""
        rospy.loginfo("[hector_ci_tools]: " + message)
