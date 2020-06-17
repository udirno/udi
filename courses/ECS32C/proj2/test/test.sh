#/bin/sh
bin_dir=../bin
data_dir=../data
${bin_dir}/proj2 ${data_dir}/num_sml_orig.txt ${data_dir}/num_sml_edit.txt > num_sml_result.txt
${bin_dir}/proj2 ${data_dir}/num_med_orig.txt ${data_dir}/num_med_edit.txt > num_med_result.txt
${bin_dir}/proj2 ${data_dir}/num_lrg_orig.txt ${data_dir}/num_lrg_edit.txt > num_lrg_result.txt
${bin_dir}/proj2 ${data_dir}/pali_orig.txt ${data_dir}/pali_sml_edit.txt > pali_sml_result.txt
${bin_dir}/proj2 ${data_dir}/pali_orig.txt ${data_dir}/pali_med_edit.txt > pali_med_result.txt
${bin_dir}/proj2 ${data_dir}/pali_orig.txt ${data_dir}/pali_lrg_edit.txt > pali_lrg_result.txt
