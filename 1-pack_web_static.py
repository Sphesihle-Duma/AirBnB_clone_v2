#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Get the current timestamp (year, month, day, hour, minute, second)
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive filename
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Compress the web_static folder into a .tgz archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the path to the created archive
        return "versions/{}".format(archive_name)

    except Exception:
        return None
