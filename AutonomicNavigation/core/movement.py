# Алексей, добавь в каждый сеттер номера порта настройку самой распберри.
# В каждый сеттер скорости/направления добавь запись в соотвествующий порт
# Обработка прерываний / стек управляющих команд (повернуть туда-то со скоростью такой-то)
class MovementSystem(object):

    def __init__(self):
        self.__is_raspberry_ok: bool = False
        # port ids for wheels directions
        self.__bl_wheel_dir_port: int = -1
        self.__br_wheel_dir_port: int = -1
        self.__fl_wheel_dir_port: int = -1
        self.__fr_wheel_dir_port: int = -1

        # 1 - forward / 0 - backward
        self.__bl_wheel_direction: int = 1
        self.__br_wheel_direction: int = 1
        self.__fl_wheel_direction: int = 1
        self.__fr_wheel_direction: int = 1

        # port ids for wheels speed
        self.__bl_wheel_speed_port: int = -1
        self.__br_wheel_speed_port: int = -1
        self.__fl_wheel_speed_port: int = -1
        self.__fr_wheel_speed_port: int = -1

        # 0 -  255 nothing but a PWM value
        self.__bl_wheel_speed: int = 0
        self.__br_wheel_speed: int = 0
        self.__fl_wheel_speed: int = 0
        self.__fr_wheel_speed: int = 0

    def __repr__(self) -> str:
        res: str = "MovementSystem:\n"
        res += f"is_raspberry_ok     : {self.__is_raspberry_ok},\n"
        res += f"bl_wheel_dir_port   : {self.__bl_wheel_dir_port},\n"
        res += f"br_wheel_dir_port   : {self.__br_wheel_dir_port},\n"
        res += f"fl_wheel_dir_port   : {self.__fl_wheel_dir_port},\n"
        res += f"fr_wheel_dir_port   : {self.__fr_wheel_dir_port},\n"

        res += f"bl_wheel_direction  : {self.__bl_wheel_direction},\n"
        res += f"br_wheel_direction  : {self.__br_wheel_direction},\n"
        res += f"fl_wheel_direction  : {self.__fl_wheel_direction},\n"
        res += f"fr_wheel_direction  : {self.__fr_wheel_direction},\n"

        res += f"bl_wheel_speed_port : {self.__bl_wheel_speed_port},\n"
        res += f"br_wheel_speed_port : {self.__br_wheel_speed_port},\n"
        res += f"fl_wheel_speed_port : {self.__fl_wheel_speed_port},\n"
        res += f"fr_wheel_speed_port : {self.__fr_wheel_speed_port},\n"

        res += f"bl_wheel_speed      : {self.__bl_wheel_speed},\n"
        res += f"br_wheel_speed      : {self.__br_wheel_speed},\n"
        res += f"fl_wheel_speed      : {self.__fl_wheel_speed},\n"
        res += f"fr_wheel_speed      : {self.__fr_wheel_speed}\n"
        return res

    __str__ = __repr__

    def __is_port_in_use(self, port_id: int):
        if self.__bl_wheel_dir_port == port_id:
            print(f"id {port_id} assigned to port : bl_wheel_dir_port")
            return True
        if self.__br_wheel_dir_port == port_id:
            print(f"id {port_id} assigned to port : br_wheel_dir_port")
            return True
        if self.__fl_wheel_dir_port == port_id:
            print(f"id {port_id} assigned to port : fl_wheel_dir_port")
            return True
        if self.__fr_wheel_dir_port == port_id:
            print(f"id {port_id} assigned to port : fr_wheel_dir_port")
            return True

        if self.__bl_wheel_speed_port == port_id:
            print(f"id {port_id} assigned to port : bl_wheel_speed_port")
            return True
        if self.__br_wheel_speed_port == port_id:
            print(f"id {port_id} assigned to port : br_wheel_speed_port")
            return True
        if self.__fl_wheel_speed_port == port_id:
            print(f"id {port_id} assigned to port : fl_wheel_speed_port")
            return True
        if self.__fr_wheel_speed_port == port_id:
            print(f"id {port_id} assigned to port : fr_wheel_speed_port")
            return True

        return False

    def is_valid(self) -> bool:

        if not self.__is_raspberry_ok:
            print("raspberry pi is not properly set up")
            return False

        if self.__bl_wheel_dir_port == -1:
            print('unassigned : bl_wheel_dir_port')
            return False
        if self.__br_wheel_dir_port == -1:
            print('unassigned : br_wheel_dir_port')
            return False
        if self.__fl_wheel_dir_port == -1:
            print('unassigned : fl_wheel_dir_port')
            return False
        if self.__fr_wheel_dir_port == -1:
            print('unassigned : fr_wheel_dir_port')
            return False

        if self.__bl_wheel_speed_port == -1:
            print('unassigned : bl_wheel_speed_port')
            return False
        if self.__br_wheel_speed_port == -1:
            print('unassigned : br_wheel_speed_port')
            return False
        if self.__fl_wheel_speed_port == -1:
            print('unassigned : fl_wheel_speed_port')
            return False
        if self.__fr_wheel_speed_port == -1:
            print('unassigned : fr_speed_speed_port')
            return False

        return True

    @property
    def back_left_wheel_dir_port(self) -> int:
        return self.__bl_wheel_dir_port

    @property
    def back_right_wheel_dir_port(self) -> int:
        return self.__br_wheel_dir_port

    @property
    def front_left_wheel_dir_port(self) -> int:
        return self.__fl_wheel_dir_port

    @property
    def front_right_wheel_dir_port(self) -> int:
        return self.__fr_wheel_dir_port

    @back_left_wheel_dir_port.setter
    def back_left_wheel_dir_port(self, port_id: int) -> None:
        if self.__is_port_in_use(port_id):
            raise RuntimeError(f"Port {port_id} already in use!")
        self.__bl_wheel_dir_port = port_id

    @back_right_wheel_dir_port.setter
    def back_right_wheel_dir_port(self, port_id: int) -> None:
        if self.__is_port_in_use(port_id):
            raise RuntimeError(f"Port {port_id} already in use!")
        self.__br_wheel_dir_port = port_id

    @front_left_wheel_dir_port.setter
    def front_left_wheel_dir_port(self, port_id: int) -> None:
        if self.__is_port_in_use(port_id):
            raise RuntimeError(f"Port {port_id} already in use!")
        self.__fl_wheel_dir_port = port_id

    @front_right_wheel_dir_port.setter
    def front_right_wheel_dir_port(self, port_id: int) -> None:
        if self.__is_port_in_use(port_id):
            raise RuntimeError(f"Port {port_id} already in use!")
        self.__fr_wheel_dir_port = port_id

    @property
    def back_left_wheel_speed_port(self) -> int:
        return self.__bl_wheel_speed_port

    @property
    def back_right_wheel_speed_port(self) -> int:
        return self.__br_wheel_speed_port

    @property
    def front_left_wheel_speed_port(self) -> int:
        return self.__fl_wheel_speed_port

    @property
    def front_right_wheel_speed_port(self) -> int:
        return self.__fr_wheel_speed_port

    @back_left_wheel_speed_port.setter
    def back_left_wheel_speed_port(self, port_id: int) -> None:
        if self.__is_port_in_use(port_id):
            raise RuntimeError(f"Port {port_id} already in use!")
        self.__bl_wheel_speed_port = port_id

    @back_right_wheel_speed_port.setter
    def back_right_wheel_speed_port(self, port_id: int) -> None:
        if self.__is_port_in_use(port_id):
            raise RuntimeError(f"Port {port_id} already in use!")
        self.__br_wheel_speed_port = port_id

    @front_left_wheel_speed_port.setter
    def front_left_wheel_speed_port(self, port_id: int) -> None:
        if self.__is_port_in_use(port_id):
            raise RuntimeError(f"Port {port_id} already in use!")
        self.__fl_wheel_speed_port = port_id

    @front_right_wheel_speed_port.setter
    def front_right_wheel_speed_port(self, port_id: int) -> None:
        if self.__is_port_in_use(port_id):
            raise RuntimeError(f"Port {port_id} already in use!")
        self.__fr_wheel_speed_port = port_id

    @property
    def back_left_wheel_speed(self) -> int:
        return self.__bl_wheel_speed

    @property
    def back_right_wheel_speed(self) -> int:
        return self.__br_wheel_speed

    @property
    def front_left_wheel_speed(self) -> int:
        return self.__fl_wheel_speed

    @property
    def front_right_wheel_speed(self) -> int:
        return self.__fr_wheel_speed

    @back_left_wheel_speed.setter
    def back_left_wheel_speed(self, speed: int) -> None:
        self.__bl_wheel_speed = min(max(0, speed), 255)

    @back_right_wheel_speed.setter
    def back_right_wheel_speed(self, speed: int) -> None:
        self.__br_wheel_speed = min(max(0, speed), 255)

    @front_left_wheel_speed.setter
    def front_left_wheel_speed(self, speed: int) -> None:
        self.__fl_wheel_speed = min(max(0, speed), 255)

    @front_right_wheel_speed.setter
    def front_right_wheel_speed(self, speed: int) -> None:
        self.__fr_wheel_speed = min(max(0, speed), 255)

    @property
    def back_left_wheel_direction(self) -> int:
        return self.__bl_wheel_speed

    @property
    def back_right_wheel_direction(self) -> int:
        return self.__br_wheel_direction

    @property
    def front_left_wheel_direction(self) -> int:
        return self.__fl_wheel_direction

    @property
    def front_right_wheel_direction(self) -> int:
        return self.__fr_wheel_direction

    @back_left_wheel_direction.setter
    def back_left_wheel_direction(self, speed: int) -> None:
        self.__bl_wheel_direction = min(max(0, speed), 1)

    @back_right_wheel_direction.setter
    def back_right_wheel_direction(self, speed: int) -> None:
        self.__br_wheel_direction = min(max(0, speed), 1)

    @front_left_wheel_direction.setter
    def front_left_wheel_direction(self, speed: int) -> None:
        self.__fl_wheel_direction = min(max(0, speed), 1)

    @front_right_wheel_direction.setter
    def front_right_wheel_direction(self, speed: int) -> None:
        self.__fr_wheel_direction = min(max(0, speed), 1)

    def set_up_wheels_directions_ports(self, bl, br, fl, fr) -> None:
        self.back_left_wheel_dir_port = bl
        self.back_right_wheel_dir_port = br
        self.front_left_wheel_dir_port = fl
        self.front_right_wheel_dir_port = fr

    def set_up_wheels_speed_ports(self, bl, br, fl, fr) -> None:
        self.back_left_wheel_speed_port = bl
        self.back_right_wheel_speed_port = br
        self.front_left_wheel_speed_port = fl
        self.front_right_wheel_speed_port = fr

    def set_up_raspberry(self) -> None:
        try:
            self.__is_raspberry_ok = True
            # any raspberry set up stuff
        except RuntimeError("Raspberry set up failed"):
            self.__is_raspberry_ok = False

    def main_movement_loop(self) -> None:
        if not self.is_valid():
            raise RuntimeError("Incorrect system set up!!!")
        while True:
            # do here any movement stuff
            pass


