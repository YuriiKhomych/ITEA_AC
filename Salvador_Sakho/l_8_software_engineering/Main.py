from Salvador_Sakho.l_8_software_engineering.Creational.entity_impl \
    .Factory_impl import RobotFactory
from Salvador_Sakho.l_8_software_engineering.Creational.entity_impl \
    .Robot_impl import RobotBuilder, RobotSoldier, NewRobot


def main():
    factory = RobotFactory()
    robot_soldier = factory.create_robot(RobotSoldier)
    robot_builder = factory.create_robot(RobotBuilder)
    new_robot = factory.create_robot(NewRobot)

    robot_soldier.listen([{'shoot': 30}])
    robot_builder.listen([{'build': 'house'}])

    robot_soldier.check_the_state('bullets')
    robot_builder.check_the_state('materials')

    new_robot.listen([{'go': 30}])


if __name__ == '__main__':
    main()
