_base_ = ['cgrseg-b_ade20k_160k.py']

model = dict(
    decode_head=dict(
        type='CGRSeg_ssa',),)