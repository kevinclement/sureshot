#!/bin/bash

echo "17" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio17/direction
echo "1" > /sys/class/gpio/gpio17/value
sleep 2
echo "0" > /sys/class/gpio/gpio17/value
echo "17" > /sys/class/gpio/unexport
