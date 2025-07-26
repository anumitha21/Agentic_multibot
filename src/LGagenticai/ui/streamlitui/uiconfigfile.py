## here this file is for , able to  read the config file 

from configparser import ConfigParser

class Config:
    def __init__(self,config_file="./src/LGagenticai/ui/streamlitui/uiconfigfile.ini"):
        self.config = ConfigParser() # this the obj of the config parser class...it will be alble to read the cinfig file
        self.config.read(config_file) # this will read the config file and store it in the config
    ## creating seperate function for each component
    def get_llm_options(self):
        return self.config['DEFAULT'].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config['DEFAULT'].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_options(self):
        return self.config['DEFAULT'].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config['DEFAULT'].get("PAGE_TITLE")