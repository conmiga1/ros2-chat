# ROS 2 Chatbot — Alice & Bob

Two ROS 2 nodes that hold a scripted conversation using a custom service.

- `alice.py` — service **client**, sends lines and prints the replies
- `bob.py` — service **server**, replies based on `Chatbot.srv`

## Requirements

- Ubuntu 24.04
- ROS 2 Jazzy

## Build

```bash
cd ~/chatbot_ws
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon build
source install/setup.bash
```

## Run

**Terminal 1 — start Bob (server) first:**
```bash
cd ~/chatbot_ws
source /opt/ros/jazzy/setup.bash
source install/setup.bash
ros2 run chatbot_nodes bob
```

**Terminal 2 — start Alice (client):**
```bash
cd ~/chatbot_ws
source /opt/ros/jazzy/setup.bash
source install/setup.bash
ros2 run chatbot_nodes alice
```

Alice will send her scripted lines one by one; the conversation prints in both terminals.
