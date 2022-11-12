pro_def_src="/home/maruti/.config/google-chrome/"
pro_1_src="/home/maruti/.config/google-chrome/Profile 1/History"
pro_2_src="/home/maruti/.config/google-chrome/Profile 2/History"
pro_dst_path="/RBKP0/kala_hdd_aiml_lab-19/skm_gitops/github/browser_analytics/raw_data/raw_profiles"
date=$(date +"%m%d%y")
cp $pro_def_src/Default/History $pro_dst_path/'PDHistory_'$date
cp $pro_def_src/Profile\ 1/History $pro_dst_path/'P1History_'$date
cp $pro_def_src/Profile\ 2/History $pro_dst_path/'P2History_'$date
