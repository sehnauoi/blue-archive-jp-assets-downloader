# Adapted from https://github.com/K0lb3/UnityPy#example

import os
import logging
import UnityPy

# set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# set up constants
BA_JP_BUNDLES_DIR = os.path.join(os.path.dirname(__file__), 'ba_jp_bundles')
BA_JP_BUNDLES_EXTRACETED_DIR = os.path.join(os.path.dirname(__file__), 'ba_jp_bundles_extracted')

# create directories
os.makedirs(BA_JP_BUNDLES_DIR, exist_ok=True)
os.makedirs(BA_JP_BUNDLES_EXTRACETED_DIR, exist_ok=True)

def unpack_all_assets(source_folder : str, destination_folder : str):
    # iterate over all files in source folder
    for root, dirs, files in os.walk(source_folder):

    
        for file_name in files:
            # generate file_path
            file_path = os.path.join(root, file_name)
            with open(file_path, 'rb') as f:
                logging.info(f'Loading {file_path}')
                # load that file via UnityPy.load
                env = UnityPy.load(f.read())

                # alternative way which keeps the original path
                for path, obj in env.container.items():
                    logger.info(f'Extracting {obj}({obj.type.name}) to {path}')
                    dest = os.path.join(destination_folder, *path.split("/"))
                    os.makedirs(os.path.dirname(dest), exist_ok = True)
                    dest, ext = os.path.splitext(dest)
                    if obj.type.name in ["Texture2D", "Sprite"]:
                        data = obj.read()
                        # create dest based on original path
                        # make sure that the dir of that path exists
                        # correct extension
                        dest = dest + ".png"
                        data.image.save(dest)
                    elif obj.type.name == "TextAsset":
                        # export asset
                        data = obj.read()
                        with open(dest, "wb") as f:
                            f.write(bytes(data.script))
                    else:
                        logger.warn(f'Unhandled asset type: {obj.type.name}')

if __name__ == '__main__':
    unpack_all_assets(BA_JP_BUNDLES_DIR, BA_JP_BUNDLES_EXTRACETED_DIR)