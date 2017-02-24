#!/bin/bash
# Program:
#       "docker Command"
# History:
# 2016/12/24    YingCheng   First release
docker run -d -P -it --name container1 -v /home/yingcheng/crawler:/forMount f88e19424d8b
docker run -d -P -it --name container2 -v /home/yingcheng/crawler:/forMount f88e19424d8b
docker run -d -P -it --name container3 -v /home/yingcheng/crawler:/forMount f88e19424d8b

docker exec -it -d  container1 python /forMount/booking.py
docker exec -it -d  container2 python /forMount/expedia.py
docker exec -it -d  container3 python /forMount/hotelcom.py
echo "=========================="
while true
do
  p1=$(docker exec -it container1 ps aux| grep 'python'|awk '{print $2}')
  p2=$(docker exec -it container2 ps aux| grep 'python'|awk '{print $2}')
  p3=$(docker exec -it container3 ps aux| grep 'python'|awk '{print $2}')
  if [ "$c1" != "" ] && [ "$c2" != "" ] && [ "$c3" != "" ] ; then
    echo "process exist!";
    sleep 3
  else
    echo "process not exist!";
    break;
  fi
done
echo "=========================="
docker rm -f `docker ps -qa`
java -jar /home/yingcheng/test/file_into_mysql.jar
echo "Congratulations!You have already succeed."
exit 0


