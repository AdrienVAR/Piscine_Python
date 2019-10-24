curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh --output inst.sh #-silent
mkdir goinfre/advardon
sh inst.sh -b -p /goinfre/advardon/miniconda

#export PATH="$HOME/miniconda/bin:$PATH"
export PATH="$/goinfre/advardon/miniconda/bin:$PATH"
#touch /usr/local/bin/python=PATH
#Expect "Please, press ENTER to continue" , put "/n"

#sleep 3
#echo | ./inst.sh
# printf "\n"
#yes | ./inst.sh
#echo -ne "\n" | "yes\n"

conda install numpy -b
conda install matplotlib -b
conda install pandas -b