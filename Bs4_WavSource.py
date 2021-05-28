lengkap=True
print("mengecek modul request")
try:
	import requests as req
except:
	lengkap=False
	print("modul request tidak ada, install dengan perintah pip3 install requests")

print("mengecek modul bs4")
try:
	from bs4 import BeautifulSoup as bs
except:
	lengkap=False
	print("modul bs4 tidak ada, install dengan perintah pip3 install beautifulsoup4")	

if lengkap:
	print("membuat koneksi....")
	header={"Host":"www.wavsource.com",
	"User-Agent":"Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
	halaman=req.get("https://www.wavsource.com/people/famous.htm",headers=header)
	print("mengambil data")
	isi_halaman=bs(halaman.text,"html.parser")
	isi_c1=isi_halaman.find_all("td",class_="c1")
	print("data didapat. menampilkan sekarang")
	for ic in isi_c1:
		isi_script=ic.find_all("script")
		if(len(isi_script)>0):
			isi_asli=str(isi_script[0])
			isi_asli=isi_asli.replace("<script type=\"text/javascript\">","")
			isi_asli=isi_asli.replace("</script>","")
			isi_asli=isi_asli.replace("s2p(","")
			isi_asli=isi_asli.replace(")","")
			isi_asli=isi_asli.replace("\'","")
			isi_asli=isi_asli.split(",")
			print("-"*10)
			print("Judul             :{}".format(isi_asli[4]))
			print("Tahun ditambahkan:{}{}".format(isi_asli[2].replace("added ",""),isi_asli[3]))
			print("link lagu        :{}/{}/{}".format("https://www.wavsource.com/snds_2020-10-01_3728627494378403",isi_asli[0],isi_asli[1]))
			print("-"*10)
