from Salvador_Sakho.l_8_software_engineering.Creational.abstract_entity \
    .Factory import AbstractFactory

from Salvador_Sakho.l_8_software_engineering.Creational \
    .entity_impl.Robot_impl import RobotSoldier, RobotBuilder, NewRobot


class RobotFactory(AbstractFactory):
    def create_robot(self, robot_class):
        value = {
            "RobotSoldier": lambda: RobotSoldier(),
            "RobotBuilder": lambda: RobotBuilder(),
            "NewRobot": lambda: NewRobot()
        }[robot_class.__name__]()
        return value
