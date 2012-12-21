#!/bin/sh
# Custom Wazapp Status Display
# by coderus
# from http://talk.maemo.org/showpost.php?p=1304621&postcount=333

reply=""
if $(qdbus | grep org.tgalal.wazapp > /dev/null)
then
        reply=`qdbus org.tgalal.wazapp /org/maemo/contextkit/Wazapp/Online org.maemo.contextkit.Property.Get | sed -n 1p`
fi

case $reply in
online) reply="В сети" ;;
connecting) reply="Подключается" ;;
offline) reply="Не в сети" ;;
*) reply="Закрыт" ;;
esac

echo -n $reply

