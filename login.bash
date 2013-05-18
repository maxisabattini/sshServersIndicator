#!/bin/bash

source $1

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
$DIR/login.expect $host $user $pass
