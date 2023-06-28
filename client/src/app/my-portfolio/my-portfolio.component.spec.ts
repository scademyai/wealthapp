import { ComponentFixture, TestBed } from '@angular/core/testing';
import { MyPortfolioComponent } from './my-portfolio.component';
import { MatGridListModule } from '@angular/material/grid-list';
import { StockCardComponent } from '../stock-card/stock-card.component';

describe('MyPortfolioComponent', () => {
  let component: MyPortfolioComponent;
  let fixture: ComponentFixture<MyPortfolioComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MyPortfolioComponent, StockCardComponent],
      imports: [MatGridListModule],
    });
    fixture = TestBed.createComponent(MyPortfolioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
