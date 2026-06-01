#!/bin/bash

tong=0

while IFS=',' read ngay doanhthu
do
    if [[ "$doanhthu" =~ ^[0-9]+$ ]]; then
        tong=$((tong + doanhthu))
    fi
done < doanhso.csv

echo "Tong doanh thu la: $tong"
