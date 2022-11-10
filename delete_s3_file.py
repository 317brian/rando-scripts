   print(f"Searching {environment} for .DS_Store files and deleting them")               
    prefix = s3info[environment][0]
    # grep returns 0 if it finds something, which is why it checks for False
    if os.system(f"aws s3 ls s3://{bucket}/{prefix}/ --recursive | grep .DS_Store") == False:
      os.system(f"aws s3 rm s3://{bucket}/{prefix}/ --recursive --exclude '*' --include '*.DS_Store'")
      print(f"Deleted them from s3://{bucket}/{prefix}/")
    else: 
      print(f"Didn't find any .DS_Store files in s3://{bucket}/{prefix}/.")
