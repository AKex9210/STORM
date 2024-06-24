#MIT License

#Copyright (c) 2024 ᴋᴜɴᴀʟ [AFK]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os
import logging
from flask import Flask
from flask_restful import Resource, Api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    api = Api(app)

    class Greeting(Resource):
        def get(self):
            logger.info("ɢʀᴇᴇᴛɪɴɢ ᴇɴᴅᴘᴏɪɴᴛ ᴡᴀꜱ ʀᴇᴀᴄʜᴇᴅ")
            return "ꜱᴛᴏʀᴍ ɪꜱ ᴜᴘ ᴀɴᴅ ʀᴇᴀᴅʏ ꜰᴏʀ ᴅᴇꜱᴛʀᴜᴄᴛɪᴏɴ!"

    api.add_resource(Greeting, '/')
    
    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"ꜱᴛᴀʀᴛɪɴɢ ꜱᴇʀᴠᴇʀ ᴏɴ ᴘᴏʀᴛ {port}")
    app.run(host="0.0.0.0", port=port)
