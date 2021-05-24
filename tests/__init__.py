import os

# Dotenv path
ENV_PATH = os.path.join(os.path.dirname(__file__), '../.env.stage')

# APOD data constants
APOD_DATA_ARG = {
    "copyright": None,
    "explanation": "Are Martians trying to tell us something?  An indentation has been recently photographed on Mars "
                   "that resembles a heart, a common human symbol for love.  Because intelligent Martians have never "
                   "been known to exist, and because formations with similarities have been found that clearly result "
                   "from natural phenomena, the pit shown above is thought not to be a form of interplanetary "
                   "communication.  Many scientists believe instead that the right-most wall of the two-kilometer "
                   "wide heart-shaped pit was created by a naturally occurring graben, a surface drop caused by "
                   "expansion along a fault-line.  Perhaps love is easier to find here on Earth.",
    "hdurl": "https://apod.nasa.gov/apod/image/9906/marsheart_mgs_big.gif",
    "mediaType": "image",
    "title": "From Mars with Love",
    "url": "https://apod.nasa.gov/apod/image/9906/marsheart_mgs.jpg"
}

APODS_DATA_ARG = [
    {
        "copyright": None,
        "explanation": "Are Martians trying to tell us something?  An indentation has been recently "
                       "photographed on Mars that resembles a heart, a common human symbol for love.  Because "
                       "intelligent Martians have never been known to exist, and because formations with similarities "
                       "have been found that clearly result from natural phenomena, the pit shown above is thought not "
                       "to be a form of interplanetary communication.  Many scientists believe instead that the "
                       "right-most wall of the two-kilometer wide heart-shaped pit was created by a naturally "
                       "occurring graben, a surface drop caused by expansion along a fault-line.  Perhaps love is "
                       "easier to find here on Earth.",
        "hdurl": "https://apod.nasa.gov/apod/image/9906/marsheart_mgs_big.gif",
        "mediaType": "image",
        "title": "From Mars with Love",
        "url": "https://apod.nasa.gov/apod/image/9906/marsheart_mgs.jpg"
    },
    {
        "copyright": None,
        "explanation": "A new mammoth telescope has begun to inspect the northern sky.  The 8-meter Gemini North "
                       "telescope, pictured above, was dedicated last week in Hawaii, with images documenting its "
                       "unprecedented abilities being released.  Within two years, sister telescope Gemini South will "
                       "begin similar observations of the southern sky from Chile.  The Gemini telescopes will collect "
                       "an enormous amount of visible and infrared light. In the infrared, a Gemini can resolve "
                       "objects that even appear blurred to the Hubble Space Telescope.  To achieve such high "
                       "resolution, the Gemini's use adaptive optics, a technique that continually flexes Gemini's "
                       "main mirrors to counteract the defocusing effects of Earth's turbulent atmosphere.  A "
                       "seven-nation collaboration is completing the Geminis under the direction of the US National "
                       "Science Foundation.",
        "hdurl": "https://apod.nasa.gov/apod/image/9906/gemini_pfa_big.jpg",
        "mediaType": "image",
        "title": "Gemini North Telescope Inaugurated",
        "url": "https://apod.nasa.gov/apod/image/9906/gemini_pfa.jpg"
    }
]
