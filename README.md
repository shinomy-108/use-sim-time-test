# use-sim-time-test

ROS2における時間の扱いについて検証するリポジトリ．

eiviroment:

- Ubuntu 22.04
- ROS2 Humble
- Gazego Fortress

## 元々の理解

- create_wall_timer()によってインスタンスされたTimerオブジェクトは"，`use_sim_time`パラメータの真偽によって，システム時間かシミュレーション時間に従う．
- `use_sim_time`パラメータが真の場合，シミュレーション時間を停止・加減速させた場合は，Timerオブジェクトのコールバック関数が呼ばれる周期もそれに従うはず．

## 実際の動作

create_wall_timer()によってインスタンスされたTimerオブジェクトを用いて，周期的にメッセージを発行するノードを作成．

### `use_sim_time:=false`

- システム時間に従って周期的にメッセージが発行されることを確認．

### `use_sim_time:=true`

- `/clock`発行のため，`Gazebo`と`ros_gz_bridge`を起動．
- `use_sim_time`パラメータが真にしてノードを起動
  - ミュレーション時間を停止・加減速させた場合でもTimerオブジェクトのコールバック関数が呼ばれる時間はそれに従わない．

<https://github.com/user-attachments/assets/0ac599dc-98f7-4fe1-8932-faf91066232f>

## 手順

`/clock`を発行するために，`Gazebo`と`ros_gz_bridge`を起動．

```bash
ros2 launch use_sim_time_test gazebo.launch.py
```

sampleノードの起動

```bash
ros2 launch use_sim_time_test sim_time_check.launch.py  use_sim_time:=true
```
