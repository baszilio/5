def medians(nums1,nums2):
    bry=nums1+nums2
    bry.sort()
    silk=len(bry)// 2
    if len(bry) % 2 == 0:
        thop= (bry[silk] + bry[silk - 1]) / 2
        return print(thop)
    elif len(nums1)== 0 and len(nums2)== 0:
        med= nums1 +nums2
        return print(med)
    else:
        thop1= bry[silk]
        return print(thop1)
