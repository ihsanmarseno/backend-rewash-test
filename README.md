# Backend Rewash Test Take Home

![image](https://github.com/user-attachments/assets/a942adef-b59e-456a-b529-44f6697870d4)

## Deskripsi
   Backend todo app memiliki fitur crud berupa create, read, update, dan delete, serta update status. Backend todo app menggunakan FastAPI untuk frameworknya dan PostgreSQL untuk database nya.

## Teknologi 
1. FastAPI
2. PostgreSQL
3. ORM Sql Alchemy

## Langkah-langkah install

1. Clone repository
   ```bash
   https://github.com/ihsanmarseno/backend-rewash-test.git
   ```

2. Install dependencies requirements
   ```bash
   pip install -r requirements.txt
   ```

3. Running aplikasi dan dapat diakses secara remote agar bisa diconsume API nya
   ```bash
   python -m uvicorn main:app --host 0.0.0.0 --port 8000
   ```

4. Buka docs swagger untuk testing
   ```bash
   http://localhost:8000/docs
   ```
   
   


