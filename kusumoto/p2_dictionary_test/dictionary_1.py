'''

'''

import csv

if __name__ == '__main__':

	place_dict = {}				#遠征先別集計用辞書:{place:{sucess:count,s_success:count,fail:count}}
	success_probability = {}	#遠征先別確率格納用辞書

	with open("testdata_ensei.csv", encoding = "cp932", newline = '') as rawDataFile:
		csvDictReader = csv.DictReader(rawDataFile)

		#a_line = next(csvDictReader)		#1行目がa_lineに代入される
		#key_view = a_line.keys()			#辞書のキー一覧がviewと呼ばれるオブジェクトで返される
		#values_view = a_line.values_list()	#辞書の値一覧がviewで返される。viewは、元となる辞書と連動している

		for a_line in csvDictReader:
			place = a_line.pop('遠征')		#キー'遠征'に対応する値を取り出す（辞書からは削除される）

			if place not in place_dict:		#今走査しているデータの遠征先名がキーとして既に存在するかどうかチェック
				place_dict[place] = {'大成功':0, '成功':0, '失敗':0}

			place_dict[place][a_line['結果']] += 1

	for place in place_dict:				#辞書をfor文で回すと、キーのリストが対象になるようだ
		num_of_trials = place_dict[place]['大成功'] + place_dict[place]['成功'] + place_dict[place]['失敗']
		super_success_prob = place_dict[place]['大成功'] / num_of_trials
		success_prob = place_dict[place]['成功'] / num_of_trials
		failure_prob = place_dict[place]['失敗'] / num_of_trials

		success_probability[place] = {'大成功率':super_success_prob, '成功率':success_prob, '失敗率':failure_prob, '総遠征回数':num_of_trials}


	print(success_probability)