declare global {
  namespace App {
    interface Platform {
      env: {
        DB: D1Database;
        INGEST_SECRET: string;
        CF_AI?: any;
      };
    }
  }
}

export {};
