pm = float(input("미세먼지(10마이크로그램)의 농도는 ?"))
if 151 <= pm:
    print("미세먼지 농도: {:.2f}, 등급: {}".format(pm, "매우나쁨"))
elif 81 <= pm:
    print("미세먼지 농도: {:.2f}, 등급: {}".format(pm, "나쁨"))
elif 31 <= pm:
    print("미세먼지 농도: {:.2f}, 등급: {}".format(pm, "보통"))
else:
    print("미세먼지 농도: {:.2f}. 등급: {}".format(pm, "좋음"))
