class configs:

    ## Application Information
    application_name = "",
    application_DID = "", ## Application ID from Discord Developers Portal

    ## Version Information
    version = "",
    version_name = "",
    version_url = "", ## Enter here url to your version file on website or repo (Don't work with Private Repo)

    ## Other Information
    devwebsite = "",
    devwebsite_name = "",
    headers = {'User-Agent': application_name + ' v' + version + " | " + version_name + " | " + '(' + devwebsite + ')'}
