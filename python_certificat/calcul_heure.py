import datetime


parse_format = "%Y%m%d"
out_format = "%Y-%m-%d"

str_1 = "20220708215959Z"

parse_date_res = datetime.datetime.strptime(str_1[:8], parse_format)

date_str_out = parse_date_res.strftime(out_format)

print(str_1)
print(date_str_out)

a=str(not_after,'utf-8')