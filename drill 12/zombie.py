import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import main_state

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

animation_names = ['Attack', 'Dead', 'Idle', 'Walk']


class Zombie:
    images = None

    def load_images(self):
        if Zombie.images is None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombiefiles/female/" + name + " (%d)" % i + ".png") for i in
                                       range(1, 11)]

    def __init__(self):
        self.x, self.y = 1280 / 4 * 3, 1024 / 4 * 3
        self.hp = 50
        self.load_images()
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = random.random() * 2 * math.pi  # random moving direction
        self.speed = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.frame = 0
        self.build_behavior_tree()
        self.target_x, self.target_y = 0, 0
        self.order = 0

    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

    def wander(self):
        # fill here
        pass

    def find_player(self):
        # fill here
        pass

    def move_to_player(self):
        # fill here
        pass

    def get_big_ball_position(self):
        big_ball = main_state.get_big_balls()
        positions = [(big_ball[i].x, big_ball[i].y) for i in range(5)]
        self.target_x, self.target_y = positions[self.order % len(positions)]
        self.order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)
        return BehaviorTree.SUCCESS

    def move_to_big_ball(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()

        distance = (self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2
        if distance < PIXEL_PER_METER ** 2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def get_small_ball_position(self):
        small_ball = main_state.get_small_balls()
        positions = [(big_ball[i].x, big_ball[i].y) for i in range(5)]
        self.target_x, self.target_y = positions[self.order % len(positions)]
        self.order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)
        return BehaviorTree.SUCCESS

    def move_to_small_ball(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()

        distance = (self.target_x - self.x)**2 + (self.target_y - self.y)**2
        if distance < PIXEL_PER_METER ** 2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def build_behavior_tree(self):
        get_big_ball_position_node = LeafNode("Get Big Ball Position", self.get_big_ball_position)
        move_to_big_ball_node = LeafNode("Move to Target", self.move_to_big_ball)
        find_big_ball_node = SequenceNode("Find Big Ball")
        find_big_ball_node.add_children(get_big_ball_position_node, move_to_big_ball_node)
        self.bt = BehaviorTree(find_big_ball_node)

    def get_bb(self):
        return self.x - 40, self.y - 50, self.x + 40, self.y + 50

    def update(self):
        self.bt.run()

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.font.draw(self.x - 60, self.y + 50, '(HP: %d)' % self.hp, (255, 255, 0))
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)

    def handle_event(self, event):
        pass
