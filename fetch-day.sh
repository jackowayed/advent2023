#!/bin/bash

aocd $1 > $1.in.txt
aocd $1 --example > $1.test.withanswer