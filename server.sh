#!/bin/sh

SOCKET=server.socket
SERVICE=server.service
PROJECT_ABS_PATH=/home/toconnell/toconnell_info/portfolio/
CMD=`which systemctl`

cd $PROJECT_ABS_PATH
echo "Working directory set to `pwd` "

case "$1" in
    enable)
        $CMD enable $PROJECT_ABS_PATH$SERVICE
        $CMD enable $PROJECT_ABS_PATH$SOCKET
        ;;
    disable)
        stop_service
        $CMD disable $SERVICE
        $CMD disable $SOCKET
        ;;
	start)
		$CMD start $SOCKET
		$CMD start $SERVICE
	;;
	stop)
		$CMD stop $SOCKET
		$CMD stop $SERVICE
	;;
esac

