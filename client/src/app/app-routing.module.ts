import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { MyPortfolioComponent } from './my-portfolio/my-portfolio.component';
import { StocksComponent } from './stocks/stocks.component';
import { StockComponent } from './stock/stock.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'my-portfolio', component: MyPortfolioComponent },
  { path: 'stocks', component: StocksComponent },
  { path: 'stock', component: StockComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
