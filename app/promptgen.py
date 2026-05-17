def generate_prompt(form):
    tujuan = form.tujuan.data.strip()
    bahasa = form.bahasa.data
    gaya = form.gaya.data
    detail = form.detail.data.strip()
    
    prompt_template = ''

    if bahasa == 'id':
        prompt_template += f"Tulis prompt untuk tujuan berikut: {tujuan}.\n"
        prompt_template += f"Gaya: {gaya}.\n"
        prompt_template += f"Detail: {detail}"
    else:
        prompt_template += f"Write a prompt for the following purpose: {tujuan}.\n"
        prompt_template += f"Style: {gaya}.\n"
        prompt_template += f"Details: {detail}"
    return prompt_template
