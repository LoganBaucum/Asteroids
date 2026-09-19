# Display settings
SCREEN_WIDTH = 1920     # TODO: dynamically get display info in future.
SCREEN_HEIGHT = 1080    # TODO: dynamically get display info in future.
MAX_FPS = 60            # TODO: dynamically get display info in future.
MAX_DELTA_TIME = 0.1    # seconds; avoids huge physics steps after a stall

# Graphics settings
LINE_WIDTH = 2

# Player settings
PLAYER_RADIUS = 20
PLAYER_SPEED = 200
PLAYER_TURN_SPEED = 300
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3
SHOT_RADIUS = 5

# Asteroid settings
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
