def domain_name(url):
      urll = url.replace("http","").replace("https" ,"").replace("www","")
      print(urll)
      dot = [i for i in range(len(urll)) if urll[i] == "."]
      print(dot)
      return urll[:dot[0]] if dot[0] >= 1 else urll[dot[0]+1 : dot[1]] 
