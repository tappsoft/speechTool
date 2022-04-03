import speech_recognition as sr
import yaml
r = sr.Recognizer()
mic = sr.Microphone()
def rec(lang='cmn-Hans-CN'):
	try:
		data={"reco":"google"}
		try:
			with open("./config.yml",encoding="utf-8")as fp:
				data=yaml.load(fp,yaml.Loader)
		except:
			pass
		with mic as source:
			r.adjust_for_ambient_noise(source,2)
			audio = r.listen(source)
			x=data.get("reco","google")
			if(x=="sphinx"):
				text=r.recognize_sphinx(audio,lang)
			if(x=="google"):
				text = r.recognize_google(audio, language=lang)
			else:
				text = r.recognize_google(audio, language=lang)
			return text
	except sr.UnknownValueError:
		return None
#