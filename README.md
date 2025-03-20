# jfkfilescanner
This is a project to webscrape the JFK files released in 2025, OCR the documents with Tesseract, and qdrant vectordb for Retrieval-Augmented Generation of the data.

## Dependencies
### Python
`Python3.11` `pytesseract` `beautifulsoup4` `tqdm`

### Bash
`popper-utils`

Optional: tesseract if you're not using pytesseract in venv

## Downloading all the PDF Files 
They Python3 file `scrapepdfs.py` will download all the PDF files for you. You need to set the page numbers when more files are released to get more as they come in. The initial release has 219 pages. 

## Extracting text data from all the PDF Files 
The `ocr.sh` contains a bach script for extracting the text from the PDF files. Keep in mind that this is not 100% accurate, as some scans were too low quality to process and some of the handwritten notes interfere with optical character recognition. None the less the output should capture 98-99% of the text for training purposes.

For journalists and influencers who need this information ASAP: You can easily `git clone` the repo and change in to the directory by doing `cd ocr_text/` on a UNIX-based system and search through the output with `grep -rni "searchterm" *` 

For example, 
```
┌─[user@computer]─[~/git/jfkfilescanner/ocr_text]
└──╼ $cd ~/git/jfkfilescanner/ocr_text/
┌─[user@computer]─[~/git/jfkfilescanner/ocr_text]
└──╼ $grep -rni "intelligence agency" *
104-10071-10010.txt:11:FROM: DIRECTOR, CENTRAL INTELLIGENCE AGENCY .
104-10072-10013.txt:12:i Be ee De a ae INTELLIGENCE AGENCY — |
104-10073-10061.txt:8:. : CENTRAL INTELLIGENCE AGENCY Co le |
104-10121-10140.txt:5:Central Intelligence Agency.
104-10122-10346.txt:6:CENTRAL INTELLIGENCE AGENCY
104-10163-10136.txt:7:CENTRAL INTELLIGENCE AGENCY e
104-10163-10140.txt:7:CENTRAL INTELLIGENCE AGENCY e
104-10163-10173.txt:7:CENTRAL INTELLIGENCE AGENCY e
104-10163-10176.txt:7:CENTRAL INTELLIGENCE AGENCY e
104-10164-10000.txt:7:CENTRAL INTELLIGENCE AGENCY e
104-10164-10002.txt:7:CENTRAL INTELLIGENCE AGENCY e
104-10177-10239.txt:7:: CENTRAL INTELLIGENCE AGENCY !
104-10178-10000.txt:7:: CENTRAL INTELLIGENCE AGENCY !
104-10178-10001.txt:7:: CENTRAL INTELLIGENCE AGENCY !
104-10178-10002.txt:7:: CENTRAL INTELLIGENCE AGENCY !
104-10179-10121.txt:11:CENTRAL INTELLIGENCE AGENCY
104-10183-10232.txt:11:. : CENTRAL INTELLIGENCE AGENCY a
104-10183-10346.txt:8:ue : en fl So CENTRAL INTELLIGENCE AGENCY Oe Stsagae * * .
104-10185-10128.txt:4:. . CENTRAL INTELLIGENCE AGENCY
104-10186-10088.txt:6:. : : . CENTRAL INTELLIGENCE AGENCY : uo
104-10186-10099.txt:7:. . . CENTRAL INTELLIGENCE AGENCY :
104-10186-10235.txt:3:o fae 4, CENTRAL INTELLIGENCE AGENCY
104-10186-10264.txt:8:. CENTRAL INTELLIGENCE AGENCY : .
104-10186-10269.txt:3:CENTRAL INTELLIGENCE AGENCY
104-10186-10308.txt:5:mad . CENTRAL INTELLIGENCE AGENCY : 7
104-10186-10309.txt:4:a : CENTRAL INTELLIGENCE AGENCY :
104-10216-10029.txt:3:7 + soe CENTRAL INTELLIGENCE AGENCY [===]: pss
104-10219-10110.txt:7:CENTRAL INTELLIGENCE AGENCY 4 H
104-10330-10102.txt:4:. Code CENTRAL INTELLIGENCE AGENCY
104-10330-10102.txt:38:the Central Intelligence Agency. In all such settings, /
124-10274-10011.txt:43:- Intelligence Agency personnel here on both an overt and covert
124-10274-10014_multirif_redacted.txt:43:- Intelligence Agency personnel here on both an overt and covert
124-10274-10029_multirif_redacted.txt:43:- Intelligence Agency personnel here on both an overt and covert
124-90041-10023.txt:10:ORIGINATOR: | CENTRAL INTELLIGENCE AGENCY
124-90065-10029.txt:11:ORIGINATOR: | CENTRAL INTELLIGENCE AGENCY :
124-90084-10077.txt:10:ORIGINATOR: CENTRAL INTELLIGENCE AGENCY
124-90110-10071.txt:10:ORIGINATOR: | CENTRAL INTELLIGENCE AGENCY ;
124-90110-10072.txt:10:| ORIGINATOR: | CENTRAL INTELLIGENCE AGENCY
124-90137-10357.txt:10:ORIGINATOR: CENTRAL INTELLIGENCE AGENCY
124-90137-10488.txt:10:ORIGINATOR: CENTRAL INTELLIGENCE AGENCY '
124-90158-10062.txt:12:ORIGINATOR: — CENTRAL INTELLIGENCE AGENCY
176-10036-10051.txt:12:| TITLE : Central Intelligence Agency Information Report
176-10036-10052.txt:11:TITLE : Central Intelligence Agency Information Report .
176-10036-10095.txt:11:TITLE : Central Intelligence Agency Information Report
176-10036-10097.txt:13:| . TITLE : Central Intelligence Agency Information Report
176-10036-10098.txt:11:. * TITLE : Central Intelligence Agency Information Report
176-10036-10099.txt:11:: TITLE : Central Intelligence Agency Information Report
180-10141-10015.txt:16:Central Intelligence Agency R di “
197-10002-10190.txt:12:ORIGINATOR : CENTRAL INTELLIGENCE AGENCY
198-10004-10076.txt:12:ORIGINATOR : CENTRAL INTELLIGENCE AGENCY
198-10004-10207.txt:12:ORIGINATOR : CENTRAL INTELLIGENCE AGENCY
```

## Committing the extracted text using qdrant/vectordb. 
(In Progress)

## Creating a backend LLM to ask questions about the 2025 JFK Files 
(Not Started)

## Creating a web front end to send requests to the backend LLM
(Not Started)

## Credits
All the original PDFs were released from the United States Government here: 
https://www.archives.gov/research/jfk/release-2025

All documents were released for public use by the National Archives and Records Administration (NARA) and declassified under Executive Order 14176. 

This is a non-commercial project under GPLv3. Feel free to use these findings in journalistic endeavors, your YouTube channel, or what not. Including the link to this project in your article or video and crediting me would be appreciated. 

There was some use of AI(OpenAI, Deepseek) to help build this AI, because it's 2025 and that happens now.

## Requests
If anyone has all of the other JFK PDF files I'd like to include those so feel free to make a pull request on the PDFs and we can just use the same script to pull all the text off all of them. 
