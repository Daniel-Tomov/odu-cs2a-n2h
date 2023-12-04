#!/bin/bash


echo Scanning $1
sudo nmap $1 -sS -sV -sC -T4 -vvv -p-