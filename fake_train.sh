#!/bin/bash
for i in $(seq 1 30); do
  echo "epoch=$i loss=0.$((RANDOM % 900 + 100))"
  sleep 1
done
echo "training done"
