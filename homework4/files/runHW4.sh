rm files/ref_output files/all_output
./inventory.py -f files/parts <files/action01 >> files/ref_output
./inventory.py -f files/parts <files/action02 >> files/ref_output
./inventory.py -f files/parts <files/action03 >> files/ref_output
./inventory.py -f files/parts <files/action04 >> files/ref_output
./inventory.py -f files/parts <files/all_actions >> files/all_output
diff -c files/ref_output files/all_output
